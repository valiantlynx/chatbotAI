<script lang="ts">
	import { page } from '$app/stores';
	import { postPocketbase, pb, getPocketbase } from '$lib/utils/api';
	import PersonalRating from './PersonalRating.svelte';
	export let data: any;

	const imageSrc = `${import.meta.env.VITE_HOST_URL}/api${data.img}?width=200&height=300`;

	// turn the views into a number by removing the commas and the last character, if the last character is a k  then multiply the number by 1000, if the last character is an m then multiply the number by 1000000
	let views = data.views;

	// remove the commas
	views = views.replace(/,/g, '');

	// check if the last character is a k or m
	const lastChar = views[views.length - 1];

	// if the last character is a k then multiply the number by 1000
	if (lastChar === 'K') {
		views = views.slice(0, views.length - 1);
		views = Number(views) * 1000;
	}

	// if the last character is an m then multiply the number by 1000000
	if (lastChar === 'M') {
		views = views.slice(0, views.length - 1);
		views = Number(views) * 1000000;
	}

	// get the genreList from pocketbase and return the id every genre that has the same name as the genre in the manga data.author array
	let genreIds: any = [];
	let authorIds: any = [];
	let pbMangaData: any = {};

	async function createOrUpdateReadingProgress(mangaId: string, chapterId: string) {
		// Check if the user is logged in
		if (pb.authStore.isValid) {
			const userId = pb.authStore.model?.id;

			// First, check if a reading progress record already exists for this manga and user
			const existingProgressList = await getPocketbase('reading_progress', {
				filter: `user="${userId}" && manga="${mangaId}"`
			});

			// If a reading progress record doesn't exist, create it
			if (existingProgressList.items.length === 0) {
				const pbData = {
					user: `${userId}`, // This is the user id, not the username
					manga: `${mangaId}`, // This is the manga id, not the manga title
					currentChapter: `${chapterId}`
				};
				await postPocketbase('reading_progress', pbData);
			} else {
				// If a reading progress record exists, update the current chapter
				const readingProgressId = existingProgressList.items[0].id;
				const data = {
					currentChapter: `${chapterId}`
				};
				await pb.collection('reading_progress').update(readingProgressId, data);
			}
		}
	}

	async function createRecord() {
		// if the user is logged in, send the manga data to pocketbase
		if (pb.authStore.isValid) {
			// Check if the manga already exists using some unique identifier, for example, the title
			const existingMangaList = await getPocketbase('mangas', {
				filter: `title="${data.title}"`
			});
			pbMangaData = existingMangaList.items[0];

			if (existingMangaList.items.length === 0) {
				// Manga doesn't exist, create it
				for (let i = 0; i < data.author.length; i++) {
					const genreList = await getPocketbase('genres', {
						filter: `name="${data.author[i]}"`
					});

					if (genreList.items.length === 0) {
						const createdAuthor = await postPocketbase('author', {
							name: `${data.author[i]}`
						});

						authorIds.push(createdAuthor.id);
					} else {
						genreIds.push(genreList.items[0].id);
					}
				}

				// create the manga data to send to pocketbase
				const pbData = {
					title: data.title,
					description: data.description,
					img: $page.url.origin + '/api' + data.img,
					updated: data.lastUpdated,
					views,
					latestChapter: data.episodes[0].chapterTitle,
					sourceid: $page.params.id,
					genres: genreIds,
					authors: authorIds,
					src: $page.url.href
				};
				const mangaRes = await postPocketbase('mangas', pbData);
				pbMangaData = mangaRes;

				// Call the function to create or update the reading progress
				await createOrUpdateReadingProgress(mangaRes.id, data.episodes[0].chapterId);
			} else {
				// Call the function to create or update the reading progress
				await createOrUpdateReadingProgress(
					existingMangaList.items[0].id,
					data.episodes[0].chapterId
				);
			}
		}
	}

	let continueFromLastReading = false;
	let continueReadingUrl: any = '';
	let progress: any = {};
	// if the user is logged in, check if the reading progress record exists, if it does make a continue reading button
	async function continueReading() {
		const existingMangaList = await getPocketbase('mangas', {
			filter: `title="${data.title}"`
		});
		pbMangaData = existingMangaList.items[0];

		if (pb.authStore.isValid) {
			const userId = pb.authStore.model?.id;

			// First, check if a reading progress record already exists for this manga and user
			const existingProgressList: any = await getPocketbase('reading_progress', {
				filter: `user="${userId}" && manga="${pbMangaData?.id}"`,
				expand: 'currentChapter'
			});

			// If a reading progress record doesn't exist, create it
			if (existingProgressList.items.length > 0) {
				// If a reading progress record exists, update the current chapter
				continueReadingUrl = existingProgressList.items[0].expand?.currentChapter.src;

				progress = existingProgressList.items[0];

				continueFromLastReading = true;
			}
		}
	}

	continueReading();
</script>

<div class="w-full flex flex-col md:flex-row gap-4">
	<!-- manga image -->
	<div class="w-full md:w-1/5 h-full">
		<a href={`${$page.url.pathname}/${data.episodes[data.episodes.length - 1].chapterId}`}>
			<img
				class="w-full h-auto object-cover rounded-lg border border-primary"
				src={imageSrc}
				alt={data.title}
			/>
		</a>
	</div>

	<!-- manga info -->
	<div class="w-full md:w-1/2 p-4 border border-primary rounded-lg shadow-md">
		<h2 class="text-xl font-bold mb-2">{data.title}</h2>
		<p class="mb-4">{data.description}</p>
		<a
			class="btn btn-primary"
			href={`${$page.url.pathname}/${data.episodes[data.episodes.length - 1].chapterId}`}
		>
			<button on:click={createRecord}>Read First</button>
		</a>
		<a class="btn btn-primary" href={`${$page.url.pathname}/${data.episodes[0].chapterId}`}>
			<button on:click={createRecord}>Read Latest</button>
		</a>
		<div class="relative">
			{#if !pb.authStore.isValid}
				<!-- Not logged in overlay -->
				<div class="absolute inset-0 flex items-center justify-center bg-primary">
					<div class="bg-base-100 z-10 p-4 rounded-lg shadow-md text-center">
						<p class="text-lg font-bold mb-4">
							Login for free to unlock auto reading-progress tracker feature:
						</p>
						<a href="/login" class="btn btn-primary">Login</a>
					</div>
				</div>
			{/if}
			{#if pb.authStore.isValid}
				<!-- logged in stats -->
				<div class="mt-4 p-4 border border-primary rounded-lg shadow-md">
					<h2 class="text-xl font-bold mb-2">Logged in as {pb.authStore.model?.username}</h2>
					<div class="grid grid-cols-2 gap-4">
						{#if continueFromLastReading}
							<a class="btn btn-primary animate-bounce" href={`${continueReadingUrl}`}>
								<button>Continue Reading</button>
							</a>
						{:else}
							<p class="text-error font-bold mb-4">
								You haven't started reading this manga yet. Read at least one chapter to start
								tracking your reading progress.
							</p>
						{/if}
						<div class="flex flex-col">
							<span class="font-bold">Current:</span>

							<span>{progress.expand?.currentChapter.chapterId}</span>
						</div>

						<div class="flex flex-col">
							<PersonalRating bind:progress />
						</div>
						<div class="flex flex-col">
							<span class="font-bold">Status:</span>
							<span>{progress.status}</span>
						</div>
						<div class="flex flex-col">
							<span class="font-bold">Completed:</span>
							<span>{progress.completed}</span>
						</div>
						<div class="flex flex-col">
							<span class="font-bold">Started:</span>
							<span>{progress.started}</span>
						</div>
					</div>
				</div>
			{:else}
				<!-- logged out stats -->
				<div
					class="mt-4 p-4 border border-primary rounded-lg shadow-md text-success bg-opacity-50 blur-sm"
				>
					<h2 class="text-xl font-bold mb-2">Logged in as {pb.authStore.model?.username}</h2>
					<div class="grid grid-cols-2 gap-4">
						{#if continueFromLastReading}
							<a class="btn btn-primary animate-bounce" href={`${continueReadingUrl}`}>
								<button>Continue Reading</button>
							</a>
						{/if}
						<div class="flex flex-col">
							<span class="font-bold">Current:</span>

							<span>{progress.expand?.currentChapter.chapterId}</span>
						</div>

						<div class="flex flex-col">
							<PersonalRating progress />
						</div>
						<div class="flex flex-col">
							<span class="font-bold">Status:</span>
							<span>{progress.status}</span>
						</div>
						<div class="flex flex-col">
							<span class="font-bold">Completed:</span>
							<span>{progress.completed}</span>
						</div>
						<div class="flex flex-col">
							<span class="font-bold">Started:</span>
							<span>{progress.started}</span>
						</div>
					</div>
				</div>
			{/if}
		</div>
	</div>

	<!-- manga stats -->
	<div class="  p-4 border border-primary rounded-lg shadow-md">
		<h2 class="text-xl font-bold mb-2">Manga Stats</h2>
		<div class="grid grid-cols-2 gap-4">
			<div class="flex flex-col">
				<span class="font-bold">Author:</span>

				<span>{data.author[0]}</span>
			</div>
			<div class="flex flex-col">
				<span class="font-bold">Genres:</span>
				{#each data.author.slice(1) as genre}
					<span>{genre}</span>
				{/each}
			</div>
			<div class="flex flex-col">
				<span class="font-bold">Artist:</span>
				<span>{data.artist}</span>
			</div>
			<div class="flex flex-col">
				<span class="font-bold">Views:</span>
				<span>{data.views}</span>
			</div>

			<div class="flex flex-col">
				<span class="font-bold">Last Updated:</span>
				<span>{data.lastUpdated}</span>
			</div>
		</div>
	</div>
</div>
