import Layout from '../templates/Layout';
import F5Table from '../components/F5Table';

export default function F5() {
  const columns = [
    { label: "Course ID / Section ID", accessor: "concat_course_id_sec_id_field", sortable: true },
    { label: "Student Name", accessor: "name", sortable: true },
  ];

  return (
    <Layout>
      <p className="text-white text-center my-4">F5. Create the list of students enrolled in a course section taught by the professor in a given semester</p>
      <F5Table tableName="F5" columns={columns} />
    </Layout>
  )
}