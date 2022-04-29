import React from "react";
import { Link, NavLink } from "react-router-dom";
import { useSignOut } from 'react-auth-kit'

const Header = () => {
    const signOut = useSignOut()

    return (
        <header className="p-4 bg-neutral-800 text-neutral-100">
            <div className="container flex justify-between h-16 mx-auto">
                <Link to="/" aria-label="Back to homepage" className="flex items-center p-2">
                    <span className="text-4xl font-extrabold text-transparent bg-clip-text bg-gradient-to-br from-emerald-600 to-blue-700">
                        UniView
                    </span>
                </Link>
                <ul className="items-stretch hidden space-x-3 lg:flex">
                <li className="flex">
                    <NavLink to="/" className={(navData) => navData.isActive ? "flex items-center px-4 -mb-1 border-b-2 border-transparent text-emerald-600 border-emerald-600" : "text-white flex items-center px-4 -mb-1 border-b-2 border-transparent" }>Home</NavLink>
                </li>
                <li className="flex">
                    <NavLink to="/instructors" className={(navData) => navData.isActive ? "flex items-center px-4 -mb-1 border-b-2 border-transparent text-emerald-600 border-emerald-600" : "text-white flex items-center px-4 -mb-1 border-b-2 border-transparent" }>Instructors</NavLink>
                </li>
                <li className="flex">
                    <NavLink to="/students" className={(navData) => navData.isActive ? "flex items-center px-4 -mb-1 border-b-2 border-transparent text-emerald-600 border-emerald-600" : "text-white flex items-center px-4 -mb-1 border-b-2 border-transparent" }>Students</NavLink>
                </li>
                <li className="flex">
                    <NavLink to="/courses" className={(navData) => navData.isActive ? "flex items-center px-4 -mb-1 border-b-2 border-transparent text-emerald-600 border-emerald-600" : "text-white flex items-center px-4 -mb-1 border-b-2 border-transparent" }>Courses</NavLink>
                </li>
                </ul>
                <div className="items-center flex-shrink-0 hidden lg:flex">
                    <button className="text-white self-center px-8 py-3 rounded" onClick={() => signOut()}>Log out</button>
                    <NavLink to="/sign_in"><button className="self-center px-8 py-3 font-semibold rounded bg-gradient-to-br from-emerald-600 to-blue-700 text-black">Sign in</button></NavLink>
                </div>
                <button className="p-4 lg:hidden">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" className="w-6 h-6 text-neutral-100">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M4 6h16M4 12h16M4 18h16"></path>
                </svg>
                </button>
            </div>
        </header>
    );
};

export default Header;