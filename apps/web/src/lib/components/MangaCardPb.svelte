<script lang="ts">
	export let manga: any;
</script>

<div
	class="w-full bg-base-300 text-base-content shadow-md rounded-xl duration-500 hover:scale-105 hover:shadow-xl border border-primary"
>
	<a class=" w-full" href={'/manga/' + manga.sourceid}>
		<img
			class=" w-full group-hover:opacity-75 overflow-hidden rounded-t-xl"
			src={manga.img}
			alt={manga.title}
		/>

		<div class="px-4 py-3 w-full">
			<span class="mr-3 uppercase text-xs truncate block text-neutral">{manga.title}</span>
			<p class="text-lg font-bold truncate block capitalize">{manga.title}</p>
			<div class="flex items-center">
				<p class="text-sm font-semibold cursor-auto truncate block text-primary">
					{manga.latestChapter}
				</p>
				<div class="ml-auto">
					<label class="cursor-auto text-secondary" for="rating-8">{manga.views}</label>
				</div>
			</div>
		</div>
	</a>
</div>
