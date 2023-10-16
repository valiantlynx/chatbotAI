<script lang="ts">
	import InputWithLabel from '$lib/components/InputWithLabel.svelte';
	import { authData } from '$lib/utils/stores';
	import { compressFileImage, patchPocketbase } from '$lib/utils/api';

	let updated: boolean;

	let data: any = {
		username: $authData.username,
		title: $authData.title,
		address: $authData.address,
		about: $authData.about,
		language: $authData.language,
		timezone: $authData.timezone,
		avatar: $authData.avatar
	};

	async function updateProfile() {
		// console.log('updateProfile from', $authData, 'to', data);
		try {
			// Convert image to compressed base64 before uploading
			const compressedImage = await compressFileImage(data.avatar, 200, 200, 0.7);
			data.avatar = compressedImage;

			const formData = new FormData();
			formData.append('data', JSON.stringify(data)); // Include the entire data object
			for (const key in data) {
				formData.append(key, data[key]);
			}

			// Exclude email and verified fields from being updated
			await patchPocketbase('users', $authData.id, formData);

			// Update authData store
			//refreshAuthPocketbase()

			// if (window){
			// 	window.location.reload()
			// }

			updated = true;
		} catch (error) {
			throw new Error('Failed to patch user.');
		}
	}

	function handleFiles(event: any) {
		data.avatar = event.target.files[0];
	}
</script>

<svelte:head>
	<title>Edit</title>
</svelte:head>

<p>Edit</p>

<div class="grid grid-cols-1 md:grid-cols-2 gap-6">
	<InputWithLabel label="username" bind:value={data.username} />
	<div class="input input-bordered flex-grow">
		{$authData.email}
		<a href="/dashboard/profile/request-email-change" class="btn btn-secondary ml-2 float-right"
			>Request Email Change
		</a>
	</div>
	<InputWithLabel label="title" bind:value={data.title} />
	<InputWithLabel label="address" bind:value={data.address} />

	<textarea
		placeholder="Type a message..."
		bind:value={data.about}
		maxlength="100"
		class="input input-bordered flex-grow h-28"
	/>

	<div class="form-control w-full max-w-xs">
		<label class="label" for="avatar-input">
			<span class="label-text">Avatar</span>
		</label>
		<input
			type="file"
			class="file-input file-input-secondary w-full max-w-xs"
			id="avatar-input"
			on:change={handleFiles}
		/>
	</div>
</div>
<div class="divider" />

<div class="grid grid-cols-1 md:grid-cols-2 gap-6">
	<InputWithLabel label="language" bind:value={data.language} />
	<InputWithLabel label="timezone" bind:value={data.timezone} />
	<div class="flex items-center">
		{#if $authData.verified}
			<span class="ml-2 text-success">Verified</span>
		{:else}
			<span class="ml-2 text-error">Not Verified</span>
		{/if}
	</div>
</div>

<div class="mt-16">
	<button class="btn btn-primary float-right" disabled={updated} on:click={updateProfile}>
		{!updated ? 'Update' : 'sent'}
	</button>
</div>
