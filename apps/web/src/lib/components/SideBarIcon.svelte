<script lang="ts">
	import Icon from '@iconify/svelte';
	export let tooltip: string;
	export let icon: any;
</script>

<div class="sidebar-icon group">
	<Icon {icon} />
	<span class="sidebar-tooltip group-hover:scale-100">
		{tooltip}
	</span>
</div>
