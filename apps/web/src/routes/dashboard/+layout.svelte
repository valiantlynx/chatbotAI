<script>
	import Login from '$lib/components/Login.svelte';
	import { pb } from '$lib/utils/api';
	import { authData } from '$lib/utils/stores';
	import { onMount } from 'svelte';
	import SideBar from '$lib/components/SideBar.svelte';

	onMount(() => {
		pb.authStore.isValid ? authData.set(pb.authStore.model) : null;
	});
</script>

{#if pb.authStore.isValid}
	<div class="flex">
		<SideBar />
		<slot />
	</div>
{:else}
	<div class="w-screen justify-center">
		<h1 class="text-center font-bold text-warning text-3xl pt-16">
			Please login to use the dashboard
		</h1>
		<Login />
	</div>
{/if}
