import React from "react";

import Header from "../components/Header";

const Layout = (props) => {
    return (
        <div className="relative bg-gradient-to-r from-stone-900 to-slate-800 min-h-screen">
            <Header />
            <main>{props.children}</main>
        </div>
    );
};

export default Layout;