<script>
	import { onMount } from 'svelte';
	let scrollPosition = 0;
	let showScrollToTop = false;

	onMount(() => {
		window.addEventListener('scroll', handleScroll);
	});

	function handleScroll() {
		scrollPosition = window.pageYOffset || document.documentElement.scrollTop;
		showScrollToTop = scrollPosition > 100;
	}

	function scrollToTop() {
		window.scrollTo({
			top: 0,
			behavior: 'smooth'
		});
	}
</script>

{#if showScrollToTop}
	<button
		class="fixed bottom-4 right-4 font-bold animate-pulse btn btn-outline btn-primary px-4 py-2 rounded-lg"
		on:click={scrollToTop}
	>
		Scroll to Top
	</button>
{/if}
