<script lang="ts">
	import { onMount } from 'svelte';
	import { page } from '$app/stores';
	import { currentPage } from '$lib/utils/stores';
	import Pagination from '$lib/components/Pagination.svelte';
	import Chapters from '$lib/components/Chapters.svelte';
	import MangaDetails from '$lib/components/MangaDetails.svelte';
	import Breadcrumbs from '$lib/components/Breadcrumbs.svelte';
	import { site } from '$lib/config/site';
	import ReadingProgress from '$lib/components/ReadingProgress.svelte';
	import Chat from '$lib/components/Chat.svelte';
	import ResponsiveBannerAd from '$lib/components/ResponsiveBannerAd.svelte';

	export let data: any;

	let { id } = $page.params;
	let chaptersPerPage = 12;
	let pageNumbers: any[] = [];
	let chaptersToShow: any[] = [];

	onMount(() => {
		updateChaptersToShow();
		generatePageNumbers();
	});

	function updateChaptersToShow() {
		const startIndex = ($currentPage - 1) * chaptersPerPage;
		const endIndex = startIndex + chaptersPerPage;

		chaptersToShow = data.episodes.slice(startIndex, endIndex);
	}

	function goToPage(event?: any) {
		currentPage.set(event.target.value);
		updateChaptersToShow();
	}

	// Generate an array of page numbers for pagination buttons
	function generatePageNumbers() {
		const totalChapters = data.episodes.length;
		const totalPages = Math.ceil(totalChapters / chaptersPerPage);
		pageNumbers = Array.from({ length: totalPages }, (_, index) => index + 1);
		return Array.from({ length: totalPages }, (_, index) => index + 1);
	}

	const crumbs = [
		{
			name: 'Home',
			url: '/'
		},
		{
			name: 'Manga',
			url: '/manga'
		},
		{
			name: data.title,
			url: '/manga/' + id
		}
	];

	// get every sentence and word in the description. into an array. so that i can use as keywords
	let description = data.description?.split(' ');
	let descriptionArray: any = [];
	let sentence = '';

	// loop through the description array and add each word to the sentence
	for (let i = 0; i < description.length; i++) {
		sentence += description[i] + ' ';

		// if the sentence is longer than 50 characters, add it to the array and reset the sentence
		if (sentence.length > 50) {
			descriptionArray.push(sentence);
			sentence = '';
		}
	}

	// if there are any words left in the sentence, add it to the array
	if (sentence.length > 0) {
		descriptionArray.push(sentence);
	}

	// if the last sentence is longer than 50 characters, split it into two sentences
	if (descriptionArray[descriptionArray.length - 1].length > 50) {
		let lastSentence = descriptionArray[descriptionArray.length - 1];
		descriptionArray[descriptionArray.length - 1] = lastSentence.slice(0, 50);
		descriptionArray.push(lastSentence.slice(50));
	}

	// if the last sentence is shorter than 50 characters, add the next sentence to it
	if (descriptionArray[descriptionArray.length - 1].length < 50) {
		let lastSentence = descriptionArray[descriptionArray.length - 1];
		descriptionArray[descriptionArray.length - 1] =
			lastSentence + descriptionArray[descriptionArray.length];
		descriptionArray.pop();
	}
</script>

<svelte:head>
	<title>{data.title}</title>
	<meta name="description" content={data.description} />
	<meta name="keywords" content={data.author + ',' + data.title + ',' + descriptionArray} />
	<meta property="og:title" content={data.title} />
	<meta property="og:description" content={data.description} />
	<meta property="og:image" content={site.protocol + site.domain + '/api' + data.img} />
	<meta property="og:url" content={site.protocol + site.domain + '/manga/' + $page.params.id} />
	<meta name="twitter:card" content="summary_large_image" />
	<meta name="twitter:site" content="@animevariant" />
	<meta name="twitter:title" content={data.title} />
	<meta name="twitter:description" content={data.description} />
	<meta name="twitter:image" content={site.protocol + site.domain + '/api' + data.img} />
	<meta name="twitter:url" content={site.protocol + site.domain + '/manga/' + $page.params.id} />
	<meta name="twitter:domain" content={site.protocol + site.domain + '/manga/' + $page.params.id} />
	<meta name="twitter:creator" content="@animevariant" />
	<meta name="twitter:image:alt" content={data.title} />
	<meta name="twitter:label5" content="Total Chapters" />
	<meta name="twitter:data5" content={data.episodes.length} />
</svelte:head>

<main class="p-8">
	<Breadcrumbs {crumbs} />
	<h1 class="text-3xl font-bold mb-6 text-center">{data.title}</h1>
	<div class="grid grid-cols-1 gap-4 m-2 p-3 w-full h-full justify-center">
		<MangaDetails {data} />
		<ResponsiveBannerAd />
		<Chapters {chaptersToShow} {id} />
		<Pagination {goToPage} {pageNumbers} />
	</div>
	<ResponsiveBannerAd />
	<Chat />
	<ResponsiveBannerAd />
	<ReadingProgress />
	<ResponsiveBannerAd />
</main>
