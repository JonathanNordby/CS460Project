import Layout from '../templates/Layout';
import F1F2Table from '../components/F1F2Table';

export default function f1_f2() {
  const columns = [
    { label: "Full Name", accessor: "name", sortable: true },
    { label: "Department Name", accessor: "dept_name", sortable: true },
    { label: "Salary", accessor: "salary", sortable: true },
  ];

  return (
    <Layout>
      <F1F2Table tableName="F1 & F2" endpoint="instructor" columns={columns} MinMaxAvg="salary" />
    </Layout>
  )
}