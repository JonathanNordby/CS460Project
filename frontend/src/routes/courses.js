import Layout from '../templates/Layout';
import Table from '../components/Table';

export default function courses() {
  const columns = [
    { label: "Title", accessor: "title", sortable: true },
    { label: "Department Name", accessor: "dept_name", sortable: true },
    { label: "Credits", accessor: "credits", sortable: true },
  ];

  return (
    <Layout>
      <Table tableName="Courses" endpoint="course" columns={columns} />
    </Layout>
  )
}