<script lang="ts">
	import { currentPage } from '$lib/utils/stores';
	export let goToPage: any;
	export let pageNumbers: any;
</script>

<div class="w-full">
	<!-- pagination -->
	<div class="join">
		<button
			class="join-item btn btn-primary"
			value={Number($currentPage) - 1}
			on:click={goToPage}
			disabled={Number($currentPage) === 1}>«</button
		>
		<select class="select select-primary w-full max-w-xs" on:change={goToPage}>
			<option disabled selected>{$currentPage}</option>
			{#each pageNumbers as pageNumber}
				{#if pageNumber !== $currentPage}
					<option value={pageNumber}>{pageNumber}</option>
				{/if}
			{/each}
		</select>
		<button
			class="join-item btn btn-primary"
			value={Number($currentPage) + 1}
			on:click={goToPage}
			disabled={Number($currentPage) === pageNumbers.length}>»</button
		>
		<!--for some reason, $currentPage is a string for the last button, so I have to convert it to a number-->
	</div>
</div>
