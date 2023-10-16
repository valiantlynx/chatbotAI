<script lang="ts">
	export let value: any;
	export let label: string;
</script>

<div class="form-control w-full">
	<label class="label" for="avatar-input">
		<span class="label-text">{label}</span>
	</label>
	<input
		type="text"
		placeholder="your place..."
		bind:value
		maxlength="100"
		class="input input-bordered flex-grow"
	/>
</div>
