const MinMaxAvg = (props) => {
    if (props.data.length === 0) return null;
    const min = Math.min(...props.data.map((item) => item[props.column]));
    const max = Math.max(...props.data.map((item) => item[props.column]));
    const avg = Math.round(props.data.reduce((acc, curr) => acc + curr[props.column], 0) / props.data.length);
    return (
        <span>Min: {min} | Max: {max} | Avg: {avg}</span>
    )
}

export default MinMaxAvg;