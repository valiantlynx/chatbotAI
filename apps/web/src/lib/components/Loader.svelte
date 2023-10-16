<script>
	let isLoading = false;

	document.addEventListener('transitionstart', () => {
		isLoading = true;
	});

	document.addEventListener('transitionend', () => {
		isLoading = false;
	});
</script>

<div class="loader" class:visible={isLoading}>
	<!-- Your loading animation or message goes here -->
	Loading...
</div>

<style>
	.loader {
		display: none;
	}

	.visible {
		display: block;
	}
</style>
