import { loadAPIData } from '@/utils/parser';
import HomePage from '@/components/HomePage';

export default function Home() {
  const data = loadAPIData();

  return <HomePage data={data} />;
}
