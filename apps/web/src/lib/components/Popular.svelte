<script lang="ts">
	import MangaCardPb from '$lib/components/MangaCardPb.svelte';
	import AnimevariantGridAds from './AnimevariantGridAds.svelte';
	import PaginationSimple from './PaginationSimple.svelte';
	import { pb } from '$lib/utils/api';
	import { popular } from '$lib/utils/stores';
	import { onMount } from 'svelte';

	let pageNo = 1;

	onMount(async () => {
		// function to get the data from the url
		const newData = async (pageNo: number) => {
			const url =
				import.meta.env.VITE_PB_URL +
				`/api/collections/reading_progress/records?page=${pageNo}&perPage=20&filter=user%3D%2277760erf1db6qql%22&expand=manga&sort=-rating`;
			const res = await fetch(url);
			const data = await res.json();
			const mangas = data.items.map((manga: any) => manga.expand?.manga);
			return mangas;
		};
		const mangas = await newData(pageNo);
		popular.set(mangas);
	});

	// Function to get the data from the URL
	const newData = async (pageNo: number) => {
		const datapb = {
			page: pageNo,
			filter: 'user="77760erf1db6qql"',
			expand: 'manga',
			sort: '-updated'
		};
		const res = await pb.collection('reading_progress').getList(1, 20, datapb);
		const mangas = res.items.map((manga) => manga.expand?.manga);
		popular.set(mangas);
		return mangas;
	};

	$: newData(pageNo);
</script>

<main class="bg-base-100 mx-4">
	<h2 class="text-2xl font-bold text-center mb-6 bg-primary rounded-lg text-primary-content">
		Popular
	</h2>
	<PaginationSimple data={$popular} bind:pageNo />

	<div class="mx-auto container gap-y-6 gap-x-4">
		{#each $popular as manga}
			<MangaCardPb {manga} />
		{/each}
	</div>

	<PaginationSimple data={$popular} bind:pageNo />
	<AnimevariantGridAds />
</main>

<style>
	.container {
		display: grid;
		grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
	}
</style>
