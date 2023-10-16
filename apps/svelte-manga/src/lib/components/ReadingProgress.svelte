<!-- ReadingProgress.svelte -->

<script lang="ts">
	import { pb, getPocketbase } from '$lib/utils/api';
	import { onMount } from 'svelte';
	import Icon from '@iconify/svelte';

	let readingProgress: any = [];

	onMount(async () => {
		if (pb.authStore.isValid) {
			const data = {
				sort: '-updated',
				filter: `user="${pb.authStore.model?.id}"`,
				expand: 'manga, currentChapter, user'
			};
			const res = await getPocketbase('reading_progress', data);
			readingProgress = res.items;
		}
	});

	// Calculate the progress percentage for each manga
	function calculateProgressPercentage(chapter: any) {
		const totalChapters = chapter.totalChapters || 1;
		const progressPercentage =
			((totalChapters - chapter.currentChapterIndex) / totalChapters) * 100;

		// Ensure the progress percentage is within the range [0, 100]
		return Math.min(100, Math.max(0, progressPercentage));
	}
</script>

<div class="bg-base-100 rounded-lg p-4 shadow-md text-base-content">
	<h2 class="text-2xl font-bold text-center mb-6 bg-primary rounded-lg text-primary-content">
		Your Reading Progress
	</h2>

	{#if pb.authStore.isValid}
		{#if readingProgress.length != 0}
			<!-- Individual Chapters -->
			<ul class="grid grid-cols-1 gap-4">
				{#each readingProgress as chapter (chapter.id)}
					<!-- Manga Card -->
					<li class="rounded-lg shadow-md border border-primary">
						<a href={`${chapter.expand?.currentChapter?.src}`} class=" hover:underline">
							<!-- Manga Cover Image -->
							<div class="card1 bg-base-300">
								<div class="card__info w-full">
									<img
										src={chapter.expand?.manga?.img}
										alt={chapter.expand?.manga?.title}
										class=" hover:underline"
									/>
									<div class="card__info--details w-full">
										<h5 class="w-full truncate block mr-3 uppercase text-xs">
											{chapter.expand?.manga?.title}
										</h5>
										<p>{chapter.expand?.currentChapter?.chapterId}/{chapter.totalChapters || 1}</p>
										<!-- Progress Bar -->
										<div class="flex items-center justify-between">
											<p class="font-bold">Progress</p>
										</div>
										<div class="relative pt-1">
											<div class="flex mb-2 items-center justify-between">
												<div>
													<span
														class="text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full bg-primary text-primary-content"
													>
														Reading
													</span>
												</div>
												<div class="text-right">
													<span class="text-xs font-semibold inline-block text-primary">
														{calculateProgressPercentage(chapter).toFixed(2)}%
													</span>
												</div>
											</div>
											<div class="flex h-2 mb-2 overflow-hidden text-xs bg-base-100 rounded">
												<div
													style={`width:${calculateProgressPercentage(chapter)}%`}
													class="shadow-none flex flex-col text-center whitespace-nowrap justify-center bg-secondary"
												/>
											</div>
										</div>
									</div>
								</div>
								<button type="button" on:click>
									<Icon icon="carbon:play-filled" />
								</button>
							</div>
						</a>
					</li>
				{/each}
			</ul>
		{:else}
			<p class="text-accent hover:underline mb-4 font-bold text-center">
				You have no reading progress.
			</p>
		{/if}
	{:else}
		<a href="/login" class="text-accent hover:underline mb-4 font-bold">
			Log In to View Reading Progress
		</a>
	{/if}
</div>

<style>
	.card1 {
		display: flex;
		justify-content: space-between;
		align-items: center;
		padding: 1em;
		box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
		border-radius: 1em;
		margin-bottom: 1em;
		animation: fade 0.4s alternate ease;
	}

	.card1:last-child {
		margin-bottom: 0;
	}

	.card1 > .card__info {
		margin-right: 0.8em;
	}

	.card1 > .card__info > img {
		width: 50px;
		margin-right: 10px;
		border-radius: 0.3em;
	}

	.card1 > .card__info {
		display: flex;
		align-items: center;
	}

	.card1 h5 {
		font-weight: 500;
		overflow: hidden;
		width: 220px;
		white-space: nowrap;
		text-overflow: ellipsis;
	}

	.card1 p {
		color: gray;
		font-size: 0.8rem;
	}

	.card1 > button {
		border: 1px solid gray;
		border-radius: 50%;
		padding: 0.5em;
	}
</style>
