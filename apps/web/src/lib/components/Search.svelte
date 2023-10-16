<script lang="ts">
	import { goto } from '$app/navigation';
	import axios from 'axios';
	import BigSearchResults from './BigSearchResults.svelte';
	import SmallSearchResults from './SmallSearchResults.svelte';
	import { metaKeywords, searchQuery } from '$lib/utils/stores';

	export let type: 'small' | 'big' = 'small';

	let searchResults: any = [];

	let searchTerm = '';

	async function search() {
		if (searchTerm.trim() === '') {
			searchResults = [];
			return;
		}

		try {
			const response = await axios.get(`${import.meta.env.VITE_HOST_URL}/api/manga/search`, {
				params: { word: searchTerm, page: 1 }
			});

			const { mangas } = response.data;

			searchResults = mangas;
		} catch (error) {
			console.error(error);
		}
	}

	let debouncedSearch: any;
	let lastSearchTerm = '';

	$: {
		if (searchTerm !== lastSearchTerm) {
			if (debouncedSearch) {
				clearTimeout(debouncedSearch);
			}

			debouncedSearch = setTimeout(search, 300);
			lastSearchTerm = searchTerm;
		}
	}

	function handleSearch(event: any) {
		searchTerm = event.target.value;
		searchQuery.set(searchTerm);
	}

	function handleClick(url: any) {
		goto(url);
		searchTerm = '';
	}
	if ($searchQuery) {
		searchTerm = $searchQuery;
	}

	// get an array of search results i can use on my meta keywords tag to improve SEO. that way, when someone searches for something, the keywords will be added to the meta keywords tag. but has a default value if there are no search results

	$: {
		if (searchResults.length > 0) {
			const keywords = searchResults.map((result: any) => result.title).join(', ');
			metaKeywords.set(keywords);
		}
	}
</script>

<div class="max-w-screen mx-auto">
	<!-- Container added here -->
	<div class="join">
		<div>
			<div>
				<input
					class="input input-bordered input-primary join-item w-full"
					value={$searchQuery && type === 'big' ? $searchQuery : ''}
					placeholder="Search"
					on:input={handleSearch}
				/>
			</div>
		</div>
		<select class="select select-bordered select-primary join-item w-1/3">
			<option disabled selected>Manga</option>
			<option disabled class="disabled:btn-error">Anime -soon</option>
			<option disabled class="disabled:btn-error">Chapters -soon</option>
			<option disabled class="disabled:btn-error">News -soon</option>
		</select>

		<a href="/manga/search" class="btn btn-primary join-item w-1/5">Search</a>
	</div>

	{#if type === 'small'}
		<SmallSearchResults {searchResults} {handleClick} />
	{:else if type === 'big'}
		<BigSearchResults {searchResults} {handleClick} />
	{/if}
</div>
