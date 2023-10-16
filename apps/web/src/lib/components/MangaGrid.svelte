<script lang="ts">
	import MangaCard from '$lib/components/MangaCard.svelte';
	import { onMount } from 'svelte';
	import AnimevariantGridAds from './AnimevariantGridAds.svelte';
	import PaginationSimple from './PaginationSimple.svelte';

	let data: any;
	let pageNo = 1;

	// function to get the data from the url
	const newData = async (pageNo: number) => {
		const url = import.meta.env.VITE_HOST_URL + `/api/manga?page=${pageNo}`;
		const res = await fetch(url);
		const data = await res.json();
		return data;
	};

	onMount(async () => {
		data = await newData(pageNo);
	});
</script>

<main class="bg-base-100 mx-4">
	<h2 class="text-2xl font-bold text-center mb-6 bg-primary rounded-lg text-primary-content">
		Latest Manga
	</h2>
	<PaginationSimple {data} bind:pageNo />
	{#await newData(pageNo)}
		<p>loading...</p>
	{:then data}
		<div class="mx-auto container gap-y-6 gap-x-4">
			{#each data.mangas as manga}
				<MangaCard {manga} />
			{/each}
		</div>
	{:catch error}
		<p>error: {error.message}</p>
	{/await}
	<PaginationSimple {data} bind:pageNo />
	<AnimevariantGridAds />
</main>

<style>
	.container {
		display: grid;
		grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
	}
</style>
