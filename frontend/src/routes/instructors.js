import Layout from '../templates/Layout';
import Table from '../components/Table';

export default function instructors() {
  const columns = [
    { label: "Full Name", accessor: "name", sortable: true },
    { label: "Department Name", accessor: "dept_name", sortable: true },
    { label: "Salary", accessor: "salary", sortable: true },
  ];

  return (
    <Layout>
      <Table endpoint="instructor" columns={columns} />
    </Layout>
  )
}