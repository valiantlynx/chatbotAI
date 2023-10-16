<script lang="ts">
	import { searchQuery } from '$lib/utils/stores';
	export let searchResults: any = [];
	export let handleClick: any;
</script>

<ul
	class="bg-base-100 w-full text-base-content rounded-box overflow-y-auto -z-0"
	hidden={$searchQuery === ''}
>
	{#if searchResults.length > 0}
		<div class="grid grid-cols-2 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4 mt-4 w-full">
			{#each searchResults as result}
				<li class="btn-ghost bg-base-300 shadow-md rounded-lg p-4 m-1">
					<button
						on:click={handleClick(result.src)}
						aria-label={'Go to ' + result.title + ' manga page'}
					>
						<h3 class="text-lg font-semibold">{result.title}</h3>
						<img src={result.img} alt={result.title} class="w-full rounded-lg mt-2" />
						<p class="text-sm mt-2">Authors: {result.author}</p>
					</button>
				</li>
			{/each}
		</div>
	{:else}
		<p>No search results</p>
	{/if}
</ul>
