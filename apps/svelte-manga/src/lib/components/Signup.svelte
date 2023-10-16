<script lang="ts">
	import { createPocketbaseUser } from '$lib/utils/api';

	let Error: boolean;
	let errorMessage: string;

	let username = '';
	let password = '';
	let email = '';

	const data = {
		username,
		email,
		emailVisibility: true,
		password,
		passwordConfirm: password
	};

	async function signup() {
		if (Error) {
			Error = false;

			return;
		}

		try {
			await createPocketbaseUser(data);
			window.location.href = '/';
		} catch (err: any) {
			Error = true;
			errorMessage = err.originalError.data.message;

			return { error: err, status: err.status };
		}
	}
</script>

<div class="relative flex flex-col items-center justify-center h-full overflow-hidden m-4">
	<div class="w-full p-6 bg-base-200 border-t-4 rounded-md shadow-md border-top lg:max-w-lg">
		<h1 class="text-3xl font-semibold text-center">AnimeVariant</h1>
		<form class="space-y-4">
			<div>
				<label class="label" for="username">
					<span class="text-base label-text">Username</span>
				</label>
				<input
					type="text"
					name="username"
					placeholder="Username"
					bind:value={data.username}
					on:input={() => (Error = false)}
					minlength="3"
					maxlength="16"
					class="input input-bordered w-full{Error ? 'input-error' : ''}"
				/>
				<label class="label" for="password">
					<span class="label-text-alt {Error ? 'text-error' : 'hidden'}"
						>We might already have a user registered with this username</span
					>
				</label>
			</div>
			<div>
				<label class="label" for="password">
					<span class="text-base label-text">Password</span>
				</label>

				<input
					type="password"
					name="password"
					placeholder="Enter Password"
					bind:value={data.password}
					on:input={() => (Error = false)}
					minlength="8"
					class="input input-bordered w-full"
				/>
			</div>
			<div>
				<label class="label" for="password">
					<span class="text-base label-text">Confirm Password</span>
				</label>

				<input
					type="password"
					name="passwordConfirm"
					placeholder="Enter Password Again"
					bind:value={data.passwordConfirm}
					on:input={() => (Error = false)}
					minlength="8"
					class="input input-bordered w-full {Error ? 'input-error' : ''}"
				/>
				<label class="label" for="password">
					<span class="label-text-alt {Error ? 'text-error' : 'hidden'}"
						>Is this your confirm password identical to your password?
					</span>
				</label>
			</div>
			<div>
				<label class="label" for="email">
					<span class="text-base label-text">Email</span>
				</label>
				<input
					bind:value={data.email}
					on:input={() => (Error = false)}
					type="email"
					placeholder="info@site.com"
					class="input input-bordered w-full {Error ? 'input-error' : ''}"
				/>
				<label class="label" for="password">
					<span class="label-text-alt {Error ? 'text-error' : 'hidden'}"
						>We might already have a user registered with this email</span
					>
				</label>
			</div>
			<h2 class=" {Error ? 'text-error' : 'hidden'}">{errorMessage} Please try again</h2>
			<br />
			<a href="/login" class=" link link-hover">Already registered? Login</a>

			<div>
				<button on:click={signup} class="btn btn-block" disabled={Error}>Sign up</button>
			</div>
		</form>
	</div>
</div>
