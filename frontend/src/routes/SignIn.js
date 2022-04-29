import React from 'react';
import Layout from '../templates/Layout';
import { useSignIn } from 'react-auth-kit'

export default function SignUp() {
	const signIn = useSignIn()
	const [formData, setFormData] = React.useState({username: '', password: ''})

	const onSubmit = (e) => {
        e.preventDefault()
		const fetchData = async () => {
            const res = await fetch("/api/token/", {
				method: 'POST',
				body: JSON.stringify(formData),
				headers: {
					'Content-Type': 'application/json'
				}
			});
            if(res.status === 200){
				const json = await res.json();
				if(signIn({
					tokenType: "Bearer",
					token: json.access,
					refreshToken: json.refresh
				})) {
					window.location.href = '/'
				} else {
					alert("Sign in failed")
				}
			} else {
				alert("Sign in failed")
			}
        };
		fetchData();
    }

	return (
		<Layout>
			<div className="flex flex-row min-h-screen justify-center items-center">
				<div className="flex flex-col justify-center max-w-md p-6 rounded-md sm:p-10 bg-neutral-900 text-neutral-100">
					<div className="mb-8 text-center">
						<h1 className="my-3 text-4xl font-bold">Sign in</h1>
						<p className="text-sm text-neutral-400">Sign in to access your account</p>
					</div>
					<form novalidate="" action="" className="space-y-12 ng-untouched ng-pristine ng-valid" data-bitwarden-watching="1" onSubmit={onSubmit}>
						<div className="space-y-4">
							<div>
								<label for="username" className="block mb-2 text-sm">Username</label>
								<input type={"username"} onChange={(e)=>setFormData({...formData, username: e.target.value})} name="username" id="username" placeholder="DaqingIsCoolz99" className="w-full px-3 py-2 border rounded-md border-neutral-700 bg-neutral-900 text-neutral-100" />
							</div>
							<div>
								<div className="flex justify-between mb-2">
									<label for="password" className="text-sm">Password</label>
								</div>
								<input type={"password"} onChange={(e)=>setFormData({...formData, password: e.target.value})} name="password" id="password" placeholder="**********" className="w-full px-3 py-2 border rounded-md border-neutral-700 bg-neutral-900 text-neutral-100" />
							</div>
						</div>
						<div className="space-y-2">
							<div>
								<button type="submit" className="w-full px-8 py-3 rounded-md bg-gradient-to-br from-emerald-600 to-blue-700 text-neutral-900">Sign in</button>
							</div>
							<p className="px-6 text-sm text-center text-neutral-400">Don't have an account yet? <a rel="noopener noreferrer" href="/sign_up" className="hover:underline text-violet-400">Sign up</a>.</p>
						</div>
					</form>
				</div>
			</div>
		</Layout>
	)
}