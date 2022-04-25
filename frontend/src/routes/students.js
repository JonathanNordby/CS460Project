import Layout from '../templates/Layout';
import Table from '../components/Table';

export default function students() {
  const columns = [
    { label: "Name", accessor: "name", sortable: true },
    { label: "Department Name", accessor: "dept_name", sortable: true },
    { label: "Total Credits", accessor: "total_credits", sortable: true },
  ];

  return (
    <Layout>
      <Table endpoint="student" columns={columns} />
    </Layout>
  )
}