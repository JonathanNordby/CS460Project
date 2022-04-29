import Layout from '../templates/Layout';
import F1F2F6Table from '../components/F1F2F6Table';

export default function F6() {
  const columns = [
    { label: "Course ID", accessor: "course_id", sortable: true },
    { label: "Title", accessor: "title", sortable: true },
    { label: "Department Name", accessor: "dept_name", sortable: true },
    { label: "Credits", accessor: "credits", sortable: true },
  ];

  return (
    <Layout>
      <F1F2F6Table tableName="F6" endpoint="course" columns={columns} />
    </Layout>
  )
}