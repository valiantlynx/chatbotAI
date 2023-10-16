<script>
	import SideBarIcon from './SideBarIcon.svelte';
	import { logoutPocketbase } from '$lib/utils/api';
</script>

<div
	class="relative top-0 left-0 px-2 w-16 h-screen bg-base-200 m-0 flex flex-col text-base-content shadow"
>
	<a href="/"><SideBarIcon tooltip="Home" icon="bx:bx-home" /></a>
	<a href="/dashboard/profile"> <SideBarIcon tooltip="Profile" icon="iconoir:profile-circle" /></a>
	<a href="/dashboard/reading-progress"
		><SideBarIcon tooltip="reading progress" icon="fluent-mdl2:reading-mode" /></a
	>
	<a href="/dashboard/settings"><SideBarIcon tooltip="Settings" icon="bx:bx-cog" /></a>
	<a href="/dashboard/upload"><SideBarIcon tooltip="Upload" icon="ph:upload-bold" /></a>
	<button on:click={logoutPocketbase}><SideBarIcon tooltip="Logout" icon="bx:bx-log-out" /></button>
</div>
