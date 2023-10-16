<script lang="ts">
	import { patchPocketbase } from '$lib/utils/api';
	export let progress: any;

	// Function to handle radio button change
	async function handleRatingChange(event: any) {
		const selectedValue = parseFloat(event.target.value);
		progress.rating = selectedValue;

		const pbData = {
			rating: progress.rating
		};
		await patchPocketbase('reading_progress', progress.id, pbData);
	}
</script>

<span class="font-bold">Rating:</span>
<div class="rating rating-lg rating-half">
	<input
		type="radio"
		name="rating-10"
		value="0"
		class="rating-hidden"
		on:change={handleRatingChange}
		checked={progress.rating === 0}
	/>
	<input
		type="radio"
		name="rating-10"
		value="0.5"
		class="bg-accent mask mask-star-2 mask-half-1"
		on:change={handleRatingChange}
		checked={progress.rating === 0.5}
	/>
	<input
		type="radio"
		name="rating-10"
		value="1"
		class="bg-accent mask mask-star-2 mask-half-2"
		on:change={handleRatingChange}
		checked={progress.rating === 1}
	/>
	<input
		type="radio"
		name="rating-10"
		value="1.5"
		class="bg-accent mask mask-star-2 mask-half-1"
		on:change={handleRatingChange}
		checked={progress.rating === 1.5}
	/>
	<input
		type="radio"
		name="rating-10"
		value="2"
		class="bg-accent mask mask-star-2 mask-half-2"
		on:change={handleRatingChange}
		checked={progress.rating === 2}
	/>
	<input
		type="radio"
		name="rating-10"
		value="2.5"
		class="bg-accent mask mask-star-2 mask-half-1"
		on:change={handleRatingChange}
		checked={progress.rating === 2.5}
	/>
	<input
		type="radio"
		name="rating-10"
		value="3"
		class="bg-accent mask mask-star-2 mask-half-2"
		on:change={handleRatingChange}
		checked={progress.rating === 3}
	/>
	<input
		type="radio"
		name="rating-10"
		value="3.5"
		class="bg-accent mask mask-star-2 mask-half-1"
		on:change={handleRatingChange}
		checked={progress.rating === 3.5}
	/>
	<input
		type="radio"
		name="rating-10"
		value="4"
		class="bg-accent mask mask-star-2 mask-half-2"
		on:change={handleRatingChange}
		checked={progress.rating === 4}
	/>
	<input
		type="radio"
		name="rating-10"
		value="4.5"
		class="bg-accent mask mask-star-2 mask-half-1"
		on:change={handleRatingChange}
		checked={progress.rating === 4.5}
	/>
	<input
		type="radio"
		name="rating-10"
		value="5"
		class="bg-accent mask mask-star-2 mask-half-2"
		on:change={handleRatingChange}
		checked={progress.rating === 5}
	/>

	<div class="dropdown dropdown-end">
		<!-- svelte-ignore a11y-no-noninteractive-tabindex -->
		<label tabindex="0" class="btn btn-circle btn-ghost btn-xs text-info" for="card-rating">
			<svg
				xmlns="http://www.w3.org/2000/svg"
				fill="none"
				viewBox="0 0 24 24"
				class="w-4 h-4 stroke-current"
				><path
					stroke-linecap="round"
					stroke-linejoin="round"
					stroke-width="2"
					d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
				/></svg
			>
		</label>
		<!-- svelte-ignore a11y-no-noninteractive-tabindex -->
		<div
			tabindex="0"
			class="card compact dropdown-content z-[1] shadow bg-base-100 rounded-box w-64"
		>
			<div class="card-body">
				<h2 class="card-title">How the rating works?</h2>
				<p>You can change the rating by clicking the rating icons!</p>
				<p>5 - masterpiece</p>
				<p>4.5 - almost masterpiece</p>
				<p>4 - really good</p>
				<p>3.5 - good</p>
				<p>3 - normal</p>
				<p>2.5 - almost bad</p>
				<p>2 - really bad</p>
				<p>1.5 - horrible</p>
				<p>1 - avoid at all costs</p>
			</div>
		</div>
	</div>
	{progress.rating}
</div>
