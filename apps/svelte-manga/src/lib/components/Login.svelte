<script lang="ts">
	import { authPocketbase, pb } from '$lib/utils/api';

	let username: string;
	let password: string;
	let Error: boolean;
	let errorMessage: string;

	async function login() {
		if (Error) {
			Error = false;

			return;
		}

		try {
			await authPocketbase(username, password);
			window.location.reload();
		} catch (err: any) {
			Error = true;

			errorMessage = err.originalError.data.message;

			return { error: err, status: err.status };
		}
	}
</script>

{#if pb.authStore.isValid}
	<div class="relative flex flex-col items-center justify-center h-screen overflow-hidden">
		<div class="w-full p-6 bg-base-200 border-t-4 rounded-md shadow-md border-top lg:max-w-lg">
			<h1 class="text-3xl font-semibold text-center">You are already logged in</h1>
			<form class="space-y-4">
				<button on:click={() => window.history.back()} class="btn btn-block btn-neutral"
					>Go back</button
				>
			</form>
		</div>
	</div>
{:else}
	<div class="relative flex flex-col items-center justify-center h-screen overflow-hidden">
		<div class="w-full p-6 bg-base-200 border-t-4 rounded-md shadow-md border-top lg:max-w-lg">
			<h1 class="text-3xl font-semibold text-center">AnimeVariant</h1>
			<form class="space-y-4">
				<div>
					<label class="label" for="username">
						<span class="text-base label-text">Username</span>
					</label>
					<input
						type="text"
						placeholder="Username"
						bind:value={username}
						on:input={() => (Error = false)}
						minlength="3"
						class="w-full input input-bordered"
					/>
				</div>
				<div>
					<label class="label" for="password">
						<span class="text-base label-text">Password</span>
					</label>

					<input
						name="password"
						bind:value={password}
						placeholder="Enter Password"
						minlength="8"
						type="password"
						on:input={() => (Error = false)}
						class="w-full input input-bordered {Error ? 'input-error' : ''}"
					/>
					<label class="label" for="password">
						<span class="label-text-alt {Error ? 'text-error' : 'hidden'}"
							>password or username incorrect</span
						>
						<span class="label-text-alt {Error ? 'text-error' : 'hidden'}"
							>are you sure your registered?</span
						>
					</label>
				</div>
				<h2 class=" {Error ? 'text-error' : 'hidden'}">{errorMessage}</h2>
				<br />
				<a href="/signup" class=" link link-hover my-2">Not registered? Signup</a>

				<div>
					<button on:click={login} class="btn btn-block" disabled={Error}>Login</button>
				</div>
			</form>
		</div>
	</div>
{/if}
