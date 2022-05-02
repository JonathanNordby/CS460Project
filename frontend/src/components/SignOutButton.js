import React from "react";
import { withSignOut } from 'react-auth-kit';

class SignOutButton extends React.Component {
    render() {
        return (
            <button onClick={() => this.props.signOut()} className="self-center px-8 py-3 font-semibold rounded bg-gradient-to-br from-emerald-600 to-blue-700 text-black">Logout</button>
        )
    }
}

export default withSignOut(SignOutButton);