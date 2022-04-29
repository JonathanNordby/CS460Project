import Layout from '../templates/Layout';
import F3Table from '../components/F3Table';

export default function F3() {
  const columns = [
    { label: "Name", accessor: "name", sortable: true },
    { label: "Department Name", accessor: "dept_name", sortable: true },
    { label: "Student Count", accessor: "studentcount", sortable: true },
  ];

  return (
    <Layout>
      <p className="text-white text-center my-4">F3. Create a table of professor name, dept, and total number of students taught by the professor in a given semester</p>
      <F3Table tableName="F3" columns={columns} />
    </Layout>
  )
}