<script>
	import Search from '$lib/components/Search.svelte';
	import { metaKeywords } from '$lib/utils/stores';
</script>

<svelte:head>
	<title>Search</title>
	<meta
		name="description"
		content="Search for manga. unlimited and free. search for manga by title or author. search for any manga you want."
	/>
	<meta
		name="keywords"
		content={`manga, search, manga search, manga search engine, manga search site, manga search website, manga search app, manga search application, manga search online, manga search free, manga search unlimited, manga search for free, manga search for unlimited, manga search for everyone, manga search for anyone, manga search for all, manga search for all users, manga search for all visitors, manga search for isekai, manga search for shounen, manga search for shoujo, manga search for seinen, manga search for josei, manga search for seinen, manga search for yuri, manga search for yaoi, manga search for ecchi, manga search for harem, manga search for romance, manga search for comedy, manga search for action, manga search for adventure, manga search for fantasy, manga search for horror, manga search for mystery, manga search for psychological, manga search for drama, manga search for slice of life, manga search for sports, manga search for mecha, manga search for sci-fi ${$metaKeywords}`}
	/>
</svelte:head>

<main class="flex flex-col items-center min-h-screen text-center bg-base-100">
	<!-- Added pb-16 for footer spacing -->
	<h1 class="text-4xl font-bold my-8">Search</h1>

	<Search type="big" />
</main>
