<script lang="ts">
	import { page } from '$app/stores';
	import { currentPage } from '$lib/utils/stores';
	export let data: any;
</script>

<div class="flex items-center justify-center mb-4">
	<button
		class="px-4 py-2 rounded-lg btn btn-primary"
		class:disabled={$currentPage === 0}
		on:click={() => ($currentPage -= 1)}
	>
		Prev
	</button>
	<h2 class="mx-4 text-lg font-bold">
		{$currentPage + 1} / {data?.images.length}
	</h2>
	<button
		class="px-4 py-2 rounded-lg btn btn-primary"
		class:disabled={$currentPage === data?.images.length - 1}
		on:click={() => ($currentPage += 1)}
	>
		Next
	</button>
</div>

<div class="flex justify-center">
	{#each data?.images as image, index}
		{#if $currentPage === index}
			<div class="w-full max-w-4xl">
				<img
					src={image.imageUrl}
					alt={`${data.title} ${$page.params.chapterid} Page ${image.pageNumber}`}
					class="w-full rounded-lg shadow-md"
				/>
			</div>
		{/if}
	{/each}
</div>
