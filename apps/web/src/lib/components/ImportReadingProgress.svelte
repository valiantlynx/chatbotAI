<script lang="ts">
	import { pb, getPocketbase, postPocketbase } from '$lib/utils/api'; // Update the import for posting reading progress
	import { addedReadingProgress } from '$lib/utils/stores'; // Import your writable store

	let uploaded: boolean;
	let jsonData: string | null = null; // Store the JSON data from the file

	async function updateReadingProgress() {
		if (pb.authStore.isValid) {
			if (jsonData) {
				try {
					const progressData = JSON.parse(jsonData);
					await readingProgress(progressData); // Post the reading progress (see src/lib/utils/api.ts
					uploaded = true;
				} catch (error) {
					console.error('Failed to post reading progress:', error);
					uploaded = false;
				}
			}
		}
	}

	function handleFiles(event: any) {
		const file = event.target.files[0];

		if (file) {
			const reader = new FileReader();
			reader.onload = (e) => {
				jsonData = e.target?.result as string;
			};
			reader.readAsText(file);
		}
	}

	// Function to create reading progress. but first create the manga and the chapter
	export const readingProgress = async (data: any) => {
		// function to update the reading status of the manga on the user record in the users collection, if the manga is not in the user record, add it, else update the reading status of the manga and the reading progress
		const genreIds: any = [];
		const authorIds: any = [];

		async function createOrUpdateReadingProgress(
			mangaId: string,
			chapterId: string,
			currentChapterIndex: number,
			totalChapters: number,
			rating: number,
			started: string,
			status: string,
			completed: string
		) {
			// Check if the user is logged in
			if (pb.authStore.isValid) {
				const userId = pb.authStore.model?.id;

				// Check if the manga already exists in the user record
				const existingProgressList = await getPocketbase('reading_progress', {
					filter: `user="${userId}" && manga="${mangaId}"`
				});

				if (existingProgressList.items.length === 0) {
					// If the manga doesn't exist, create it
					const pbData = {
						user: `${userId}`, // This is the user id, not the username
						manga: `${mangaId}`, // This is the manga id, not the manga title
						currentChapter: `${chapterId}`,
						currentChapterIndex: currentChapterIndex,
						totalChapters: totalChapters,
						rating: rating,
						started: started,
						status: status,
						completed: completed
					};
					await postPocketbase('reading_progress', pbData);
				} else {
					// If a reading progress record exists, update the current chapter
					const readingProgressId = existingProgressList.items[0].id;
					const pbdata = {
						currentChapter: `${chapterId}`,
						currentChapterIndex: currentChapterIndex,
						totalChapters: totalChapters,
						rating: rating,
						started: started,
						status: status,
						completed: completed
					};
					await pb.collection('reading_progress').update(readingProgressId, pbdata);
				}
			}
		}

		async function search(entry: any) {
			try {
				const response = await fetch(
					`${import.meta.env.VITE_HOST_URL}/api/manga/search?word=${entry.name}&page=${1}`
				);

				const data = await response.json();
				const mangas = data.mangas;
				return mangas[0];
			} catch (error) {
				console.error(error);
			}
		}

		async function chaptersIndex(chapterid: string, id: string) {
			const url = `/manga/${id}/chapter-${chapterid}`;

			try {
				const response = await fetch(
					import.meta.env.VITE_HOST_URL + `/api/manga/${id}/${chapterid}?url=${url}`
				);
				const data = await response.json();

				const currentChapterIndex = data.chapters?.findIndex(
					(chapter: any) => chapter.value === url?.replace('/manga', '')
				);
				const totalChapters = data.chapters?.length;
				return { currentChapterIndex, totalChapters };
			} catch (error) {
				console.error(error);
				return { currentChapterIndex: 1, totalChapters: 1 };
			}
		}

		async function createRecord(entry: any) {
			const manga = await search(entry);
			// if the user is logged in, send the chapter data to pocketbase
			if (pb.authStore.isValid) {
				// Check if the manga already exists using some unique identifier, for example, the title
				const existingChapterList = await getPocketbase('Chapters', {
					filter: `src="${manga?.src}"`
				});

				if (existingChapterList.items.length === 0) {
					// Check if the manga already exists using some unique identifier, for example, the title
					const existingMangaList = await getPocketbase('mangas', {
						filter: `sourceid~"${manga?.mangaParkId}"`
					});
					// If a manga record doesn't exist, create it
					if (existingMangaList.items.length === 0) {
						const urlmanga = `/manga/${manga?.mangaParkId}`;

						const responsemanga = await fetch(
							import.meta.env.VITE_HOST_URL + `/api/manga/${manga?.mangaParkId}?url=${urlmanga}`
						);
						const datamanga = await responsemanga.json();

						// Manga doesn't exist, create it
						for (let i = 0; i < datamanga.author?.length; i++) {
							const genreList = await getPocketbase('genres', {
								filter: `name="${datamanga.author[i]}"`
							});

							if (genreList.items?.length === 0) {
								const createdAuthor = await postPocketbase('author', {
									name: `${datamanga.author[i]}`
								});

								authorIds.push(createdAuthor.id);
							} else {
								genreIds.push(genreList.items[0].id);
							}
						}

						// create the manga datamanga to send to pocketbase
						const pbDataManga = {
							title: datamanga.title,
							description: datamanga.description,
							img: import.meta.env.VITE_HOST_URL + '/api' + datamanga.img,
							updated: datamanga.lastUpdated,
							views: datamanga.views,
							latestChapter: datamanga.episodes[0]?.chapterTitle,
							sourceid: manga?.mangaParkId,
							genres: genreIds,
							authors: authorIds,
							src: manga?.src
						};
						const mangaRes = await postPocketbase('mangas', pbDataManga);
						// create the chapter data to send to pocketbase
						const pbData = {
							title: entry.name,
							chapterId: `chapter-${entry.ch ? entry.ch : 1}`,
							src:
								import.meta.env.VITE_HOST_URL +
								`/manga/${manga?.mangaParkId}/chapter-${entry.ch ? entry.ch : 1}`,
							manga: mangaRes.id
						};
						const chapterRes = await postPocketbase('Chapters', pbData);

						const { currentChapterIndex, totalChapters } = await chaptersIndex(
							entry.ch ? entry.ch : 1,
							manga?.mangaParkId
						);
						// Call the function to create or update the reading progress
						await createOrUpdateReadingProgress(
							chapterRes.manga,
							chapterRes.id,
							currentChapterIndex,
							totalChapters,
							entry.rating,
							entry.started,
							entry.status,
							entry.completed
						);
					} else {
						// create the chapter data to send to pocketbase
						const pbData = {
							title: entry.name,
							chapterId: `chapter-${entry.ch ? entry.ch : 1}`,
							src:
								import.meta.env.VITE_HOST_URL +
								`/manga/${manga?.mangaParkId}/chapter-${entry.ch ? entry.ch : 1}`,
							manga: existingMangaList.items[0].id
						};
						const chapterRes = await postPocketbase('Chapters', pbData);

						const { currentChapterIndex, totalChapters } = await chaptersIndex(
							entry.ch ? entry.ch : 1,
							manga?.mangaParkId
						);
						// Call the function to create or update the reading progress
						await createOrUpdateReadingProgress(
							chapterRes.manga,
							chapterRes.id,
							currentChapterIndex,
							totalChapters,
							entry.rating,
							entry.started,
							entry.status,
							entry.completed
						);
					}
				} else {
					const { currentChapterIndex, totalChapters } = await chaptersIndex(
						entry.ch ? entry.ch : 1,
						manga?.mangaParkId
					);
					// Call the function to create or update the reading progress
					await createOrUpdateReadingProgress(
						existingChapterList.items[0].manga,
						existingChapterList.items[0].id,
						currentChapterIndex,
						totalChapters,
						entry.rating,
						entry.started,
						entry.status,
						entry.completed
					);
				}
			}
		}

		for (let i = 0; i < data.entries.length; i++) {
			await createRecord(data.entries[i]);
			const log: any = `created: ${data.entries[i].name} ${i + 1} of ${data.entries.length}`;
			const logdata = {
				log: log,
				time: new Date().toLocaleString(),
				progress: i + 1,
				total: data.entries.length
			};
			addedReadingProgress.update((n) => [...n, logdata]);
		}
	};
</script>

<svelte:head>
	<title>Import Reading Progress</title>
</svelte:head>

<div
	class="container mx-auto p-4 sm:p-8 max-w-xl border border-primary rounded-r-lg shadow-md w-full lg:w-1/4"
>
	<h2 class="text-3xl font-semibold text-center mb-6">Import Reading Progress</h2>
	<div class="form-control mb-7">
		<label class="label" for="progress-input">
			<span class="label-text font-bold">JSON File</span>
		</label>
		<input
			type="file"
			class="file-input file-input-primary w-full max-w-xs"
			id="progress-input"
			on:change={handleFiles}
		/>
	</div>

	<!-- Progress Log Display -->
	<div class="mb-6">
		<h2 class="text-xl font-semibold">
			Progress Log:
			<p class="text-success text-sm">
				{$addedReadingProgress[$addedReadingProgress.length - 1]?.progress} of {$addedReadingProgress[1]
					?.total}
			</p>
		</h2>

		<div class="border border-primary rounded p-2 h-40 overflow-y-auto scroll-m-3">
			{#each $addedReadingProgress as progress (progress)}
				<p class="text-sm truncate text-warning">
					{progress.log}
				</p>
			{/each}
		</div>
	</div>

	<div class="flex justify-end">
		<button
			class="btn btn-primary"
			disabled={!jsonData || uploaded}
			on:click={updateReadingProgress}
		>
			{!uploaded ? 'Upload' : 'Sent'}
		</button>
	</div>
</div>
