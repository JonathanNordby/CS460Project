import Layout from '../templates/Layout';
import F4Table from '../components/F4Table';

export default function F3() {
  const columns = [
    { label: "Course ID", accessor: "course_id", sortable: true },
    { label: "Section ID", accessor: "sec_id", sortable: true },
    { label: "Sectioned Students", accessor: "sectionedstudents", sortable: true },
  ];

  return (
    <Layout>
      <p className="text-white text-center my-4">F4. Create the list of course sections and the number of students enrolled in each section that the professor taught in a given semester</p>
      <F4Table tableName="F4" columns={columns} />
    </Layout>
  )
}