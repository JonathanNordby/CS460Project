import Layout from '../templates/Layout';

export default function SignUp() {
	return (
		<Layout>
			<div className="flex flex-row min-h-screen justify-center items-center">
				<div className="flex flex-col justify-center max-w-md p-6 rounded-md sm:p-10 bg-neutral-900 text-neutral-100">
					<div className="mb-8 text-center">
						<h1 className="my-3 text-4xl font-bold">Sign in</h1>
						<p className="text-sm text-neutral-400">Sign in to access your account</p>
					</div>
					<form novalidate="" action="" className="space-y-12 ng-untouched ng-pristine ng-valid" data-bitwarden-watching="1">
						<div className="space-y-4">
							<div>
								<label for="email" className="block mb-2 text-sm">Email address</label>
								<input type="email" name="email" id="email" placeholder="acollins@clarkson.edu" className="w-full px-3 py-2 border rounded-md border-neutral-700 bg-neutral-900 text-neutral-100" />
							</div>
							<div>
								<div className="flex justify-between mb-2">
									<label for="password" className="text-sm">Password</label>
								</div>
								<input type="password" name="password" id="password" placeholder="**********" className="w-full px-3 py-2 border rounded-md border-neutral-700 bg-neutral-900 text-neutral-100" />
							</div>
						</div>
						<div className="space-y-2">
							<div>
								<button type="button" className="w-full px-8 py-3 rounded-md bg-gradient-to-br from-emerald-600 to-blue-700 text-neutral-900">Sign in</button>
							</div>
							<p className="px-6 text-sm text-center text-neutral-400">Don't have an account yet? <a rel="noopener noreferrer" href="/sign_up" className="hover:underline text-violet-400">Sign up</a>.</p>
						</div>
					</form>
				</div>
			</div>
		</Layout>
	)
}