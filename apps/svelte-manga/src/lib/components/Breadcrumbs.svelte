<script lang="ts">
	export let crumbs: any = [];
</script>

<div class="text-sm breadcrumbs m-4 text-center">
	<ul>
		{#each crumbs as crumb}
			<li>
				<a href={crumb.url} class="link link-hover">
					{crumb.name}
				</a>
			</li>
		{/each}
	</ul>
</div>
