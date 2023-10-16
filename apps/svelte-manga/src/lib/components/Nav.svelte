<script>
	import Search from './Search.svelte';
	import ProfileModal from './ProfileModal.svelte';
	import { page } from '$app/stores';
	import ThemeChanger from './ThemeChanger.svelte';
</script>

<!-- Small Devices Layout -->
<div>
	<div class="navbar bg-base-300 max-w-full sm:hidden">
		<div class="flex-1">
			<a class="btn btn-ghost normal-case text-xl" href="/">AnimeVariant</a>
			<ThemeChanger />
		</div>
		<ProfileModal />
	</div>
	<!-- Show search bar only on pages other than search -->
	{#if $page.url.pathname !== '/manga/search'}
		<div class="navbar bg-base-300 flex flex-col sm:hidden">
			<div class="flex-none sm:flex sm:gap-2">
				<Search type="small" />
			</div>
		</div>
	{/if}
</div>

<!-- Large Devices Layout -->
<div class="navbar bg-base-300 hidden sm:flex">
	<div class="flex-1">
		<a class="btn btn-ghost normal-case text-xl" href="/">AnimeVariant</a>
		<ThemeChanger />
	</div>
	<div class="flex-none gap-2">
		<!-- Show search bar only on pages other than search -->
		{#if $page.url.pathname !== '/manga/search'}
			<Search type="small" />
		{/if}
		<ProfileModal />
	</div>
</div>
