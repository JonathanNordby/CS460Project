import Layout from '../templates/Layout';
import F1F2F6Table from '../components/F1F2F6Table';

export default function f1_f2() {
  const columns = [
    { label: "Full Name", accessor: "name", sortable: true },
    { label: "Department Name", accessor: "dept_name", sortable: true },
    { label: "Salary", accessor: "salary", sortable: true },
  ];

  return (
    <Layout>
      <p className="text-white text-center my-4">F1. Create a list of professors sorted by one of the following criteria chosen by the admin: (1) by name (2) by dept, or (3) by salary
      <br />
      F2. Create a table of min/max/average salaries by dept</p>
      <F1F2F6Table tableName="F1 & F2" endpoint="instructor" columns={columns} MinMaxAvg="salary" />
    </Layout>
  )
}