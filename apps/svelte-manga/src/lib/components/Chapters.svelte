<script lang="ts">
	import ChapterCard from './ChapterCard.svelte';
	import ResponsiveBannerAd from './ResponsiveBannerAd.svelte';
	export let chaptersToShow: any;
	export let id: any;
</script>

<div class="w-full">
	<!-- chapters -->
	<div class="grid gap-4 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5">
		{#each chaptersToShow as chapter}
			<ChapterCard {chapter} url={`/manga/${id}/${chapter.chapterId}`} />
		{/each}
		<ResponsiveBannerAd />
	</div>
</div>
