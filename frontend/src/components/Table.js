import React, { useEffect, useState } from "react";

import TableBody from "./TableBody";
import TableHead from "./TableHead";
import MinMaxAvg from "./MinMaxAvg";

const Table = (props) => {
    const [origTableData, setOrigTableData] = useState([]);
    const [tableData, setTableData] = useState([]);
    const [isLoading, setIsLoading] = useState(false);

    useEffect(() => {
        const fetchData = async () => {
            setIsLoading(true);
            const response = await fetch("/api/" + props.endpoint + "/");
            const json = await response.json();
            setOrigTableData(json);
            setTableData(json);
            setIsLoading(false);
        };
        fetchData();
    }, [props.endpoint, setTableData]);

    const depts = [...new Set(origTableData.map(item => item.dept_name))].sort();

    const handleFiltering = (e) => {
        const filteredData = origTableData.filter(item => item.dept_name === e.target.value);
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

    const minMaxAvgs = (typeof props.MinMaxAvg !== 'undefined' && props.MinMaxAvg) ? props.MinMaxAvg.split(",") : [];

    return (
        <React.Fragment>
            {isLoading ? (
                <p>Loading ...</p>
            ) : (
                <div className="container p-2 mx-auto sm:p-4 dark:text-neutral-100">
                    <h2 className="mb-4 text-2xl font-semibold leading-tight text-white">{props.tableName}</h2>
                    Department: <select onChange={handleFiltering} class="form-select appearance-none block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding bg-no-repeat border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none">
                        {depts.map((dept) => {
                            return <option value={dept}>{dept}</option>;
                        })}
                    </select>
                    <br />
                    <div className="overflow-x-auto">
                        <table className="min-w-full text-xs">
                            <TableHead columns={props.columns} handleSorting={handleSorting} />
                            <TableBody columns={props.columns} tableData={tableData} />
                        </table>
                    </div>
                    {minMaxAvgs.map((minMaxAvg) => {
                        return <MinMaxAvg data={tableData} column={minMaxAvg} />;
                    })}
                </div>
            )}
        </React.Fragment>
    );
};

export default Table;
