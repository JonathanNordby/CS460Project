const TableBody = (props) => {
  return (
    <tbody>
      {props.tableData.map((data) => {
        return (
          <tr key={data.id} className="border-b border-opacity-20 border-neutral-700 bg-neutral-900">
            {props.columns.map(({ accessor }) => {
              const tData = data[accessor] ? data[accessor] : "——";
              return <td key={accessor} className="p-3 text-white">{tData}</td>;
            })}
          </tr>
        );
      })}
    </tbody>
  );
};

export default TableBody;
