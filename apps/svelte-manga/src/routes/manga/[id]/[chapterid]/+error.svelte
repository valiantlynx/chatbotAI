<script>
	import { page } from '$app/stores';

	function goBack() {
		window.history.back();
	}
</script>

<main class="p-8 text-center">
	<h1 class="text-2xl font-bold mb-4">{$page.status}: {$page.error?.message}</h1>
	<button
		class="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded"
		on:click={goBack}>Go Back</button
	>
</main>
