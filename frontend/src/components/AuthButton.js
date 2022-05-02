import React from "react";
import { withAuthHeader } from 'react-auth-kit';
import { NavLink } from "react-router-dom";

import SignOutButton from "./SignOutButton";

class AuthButton extends React.Component {
    render() {
        if (this.props.authHeader) {
            return (
                <SignOutButton />
            )
        } else {
            return (
                <NavLink to="/sign_in"><button className="self-center px-8 py-3 font-semibold rounded bg-gradient-to-br from-emerald-600 to-blue-700 text-black">Sign in</button></NavLink>
            )
        }
    }
}

export default withAuthHeader(AuthButton);