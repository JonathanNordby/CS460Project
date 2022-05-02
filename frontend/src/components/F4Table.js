import React, { useEffect, useState } from "react";
import { withAuthHeader } from 'react-auth-kit'

import TableBody from "./TableBody";
import TableHead from "./TableHead";

const F4Table = (props) => {
    const [tableData, setTableData] = useState([]);
    const [isLoading, setIsLoading] = useState(false);
    const [semesterView, setSemesterView] = useState(false);

    useEffect(() => {
        if (props.authHeader == null || props.authHeader === "" || typeof props.authHeader === 'undefined') {
            alert("You must be logged in to view this page.")
            window.location.href = "/sign_in"
        } else {
            const fetchData = async () => {
                setIsLoading(true);
                const endpoint = (typeof semesterView !== 'undefined' && semesterView) ? semesterView : 'func4f'
                const response = await fetch("/api/" + endpoint + "/", { headers: {'Authorization': props.authHeader } });
                if (response.status !== 200) {
                    alert("You do not have access to view this page.")
                    window.location.href = "/"
                } else {
                    const json = await response.json();
                    setTableData(json);
                    setIsLoading(false);
                }
            };
            fetchData();
        }
    }, [semesterView, setTableData, props.authHeader]);

    const handleSemester = (e) => {
        setSemesterView(e.target.value);
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
                    Semester: <select defaultValue={semesterView} onChange={handleSemester} className="form-select appearance-none block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding bg-no-repeat border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none">
                            <option value="func4f">Fall 2020</option>
                            <option value="func4s">Spring 2020</option>
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

export default withAuthHeader(F4Table);
