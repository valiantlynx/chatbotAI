<script lang="ts">
	export let data: any;
	export let pageNo: number;
</script>

<div class="flex justify-center my-2">
	<div class="join grid grid-cols-2 w-1/4">
		<button
			class="join-item btn btn-primary border-secondary"
			on:click={() => pageNo--}
			disabled={pageNo === 1}
		>
			Previous - {pageNo - 1}
		</button>
		<button
			class="join-item btn btn-primary border-secondary animate-pulse"
			on:click={() => pageNo++}
			disabled={!data}
		>
			Next - {pageNo + 1}
		</button>
	</div>
</div>
