<script>
	import { authData } from '$lib/utils/stores';
	import { logoutPocketbase, pb } from '$lib/utils/api';
	import { page } from '$app/stores';
	import { site } from '$lib/config/site';

	const avatar = pb.authStore.model?.avatar
		? `${site.pocketbase}/api/files/_pb_users_auth_/${pb.authStore.model?.id}/${pb.authStore.model?.avatar}`
		: `https://avatars.dicebear.com/api/adventurer-neutral/${pb.authStore.model?.username}.svg`;
</script>

<!-- profile-->
{#if pb.authStore.isValid}
	<div class="dropdown dropdown-end">
		<!-- svelte-ignore a11y-no-noninteractive-tabindex -->
		<label tabindex="0" for="profile button" class="btn btn-ghost btn-circle avatar">
			<div class="w-10 rounded-full">
				<img
					src={avatar}
					alt={`${$authData.username} profile picture on ${site.title}, ${
						site.protocol + site.domain
					}`}
				/>
			</div>
		</label>
		<!-- svelte-ignore a11y-no-noninteractive-tabindex -->
		<ul
			tabindex="0"
			class="menu menu-sm dropdown-content mt-3 z-[1] p-2 shadow bg-base-100 rounded-box w-52"
		>
			<li>
				<a class="justify-between" href="/dashboard/profile/preview">
					Profile
					<span class="badge">New</span>
				</a>
			</li>
			<li aria-current={$page.url.pathname === '/' ? 'page' : undefined}>
				<a href="/">Home</a>
			</li>
			<li aria-current={$page.url.pathname === '/dashboard' ? 'page' : undefined}>
				<a class="justify-between" href="/dashboard">
					Dashboard
					<span class="badge">New</span>
				</a>
			</li>
			<li aria-current={$page.url.pathname === '/dashboard/reading-progress' ? 'page' : undefined}>
				<a class="justify-between" href="/dashboard/reading-progress">
					Reading Progress
					<span class="badge">New</span>
				</a>
			</li>
			<li>
				<button class="signout-button bg-error opacity-80" on:click={logoutPocketbase}
					>Sign Out</button
				>
			</li>
		</ul>
	</div>
{:else}
	<a href="/login" class="btn btn-primary">login</a>
{/if}
