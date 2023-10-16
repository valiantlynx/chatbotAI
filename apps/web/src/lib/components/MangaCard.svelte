<script lang="ts">
	import { page } from '$app/stores';
	export let manga: any;

	const imageSrc = `${import.meta.env.VITE_HOST_URL}/api${manga.img}?width=200&height=300`;
</script>

<div
	class="w-full bg-base-300 text-base-content shadow-md rounded-xl duration-500 hover:scale-105 hover:shadow-xl border border-primary"
>
	<a class=" w-full" href={$page.url.origin + '/manga/' + manga.id}>
		<img
			class=" w-full group-hover:opacity-75 overflow-hidden rounded-t-xl"
			src={imageSrc}
			alt={manga.title}
		/>

		<div class="px-4 py-3 w-full">
			<span class="mr-3 uppercase text-xs truncate block text-neutral">{manga.author[0]}</span>
			<p class="text-lg font-bold truncate block capitalize">{manga.title}</p>
			<div class="flex items-center">
				<p class="text-sm font-semibold cursor-auto truncate block text-primary">
					{manga.latestChapter}
				</p>
				<div class="ml-auto">
					<div class="rating rating-sm">
						<label class="cursor-auto text-secondary" for="rating-8">{manga.rating}</label>
						<input type="radio" name="rating-8" class="mt-1 mask mask-star-2 bg-info" checked />
					</div>
				</div>
			</div>
		</div>
	</a>
</div>
