<script lang="ts">
	import { page } from '$app/stores';
	export let data: any;
</script>

<div class="flex flex-wrap justify-center gap-4 max-w-full mx-auto">
	{#each data?.images as image}
		<div class="w-full md:w-1/2 lg:w-1/3 xl:w-1/4">
			<img
				src={image.imageUrl}
				alt={`${data.title} ${$page.params.chapterid} Page ${image.pageNumber}`}
				class="w-full rounded-lg shadow-md"
			/>
		</div>
	{/each}
</div>
