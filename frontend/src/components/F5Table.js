import React, { useEffect, useState } from "react";
import { withAuthHeader } from 'react-auth-kit'

import TableBody from "./TableBody";
import TableHead from "./TableHead";

const F5Table = (props) => {
    const [origTableData, setOrigTableData] = useState([]);
    const [tableData, setTableData] = useState([]);
    const [isLoading, setIsLoading] = useState(false);

    useEffect(() => {
        if (props.authHeader == null || props.authHeader === "" || typeof props.authHeader === 'undefined') {
            alert("You must be logged in to view this page.")
            window.location.href = "/sign_in"
        } else {
            const fetchData = async () => {
                setIsLoading(true);
                const response = await fetch("/api/func5/", { headers: {'Authorization': props.authHeader } });
                if (response.status !== 200) {
                    alert("You do not have access to view this page.")
                    window.location.href = "/"
                } else {
                    const json = await response.json();
                    setOrigTableData(json);
                    setTableData(json);
                    setIsLoading(false);
                }
            };
            fetchData();
        }
    }, [setTableData, props.authHeader]);

    const sections = [...new Set(origTableData.map(item => item.concat_course_id_sec_id_field))].sort();

    const handleFiltering = (e) => {
        const filteredData = origTableData.filter(item => item.concat_course_id_sec_id_field === e.target.value);
        setTableData(filteredData);
    }

    const handleSorting = (sortField, sortOrder) => {
        if (sortField) {
            const sorted = [...tableData].sort((a, b) => {
                if (a[sortField] === null) return 1;
                if (b[sortField] === null) return -1;
                if (a[sortField] === null && b[sortField] === null) return 0;
                return (
                    a[sortField].toString().localeCompare(b[sortField].toString(), "en", {
                        numeric: true,
                    }) * (sortOrder === "asc" ? 1 : -1)
                );
            });
            setTableData(sorted);
        }
    };

    return (
        <React.Fragment>
            {isLoading ? (
                <p>Loading ...</p>
            ) : (
                <div className="container p-2 mx-auto sm:p-4 dark:text-neutral-100">
                    <h2 className="mb-4 text-2xl font-semibold leading-tight text-white">{props.tableName}</h2>
                    Section: <select onChange={handleFiltering} className="form-select appearance-none block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding bg-no-repeat border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none">
                        {sections.map((section) => {
                            return <option value={section}>{section}</option>;
                        })}
                    </select>
                    <br />
                    <div className="overflow-x-auto">
                        <table className="min-w-full text-xs">
                            <TableHead columns={props.columns} handleSorting={handleSorting} />
                            <TableBody columns={props.columns} tableData={tableData} />
                        </table>
                    </div>
                </div>
            )}
        </React.Fragment>
    );
};

export default withAuthHeader(F5Table);
