'use client';
import { useEffect, useState } from 'react';
import { useRouter } from 'next/navigation';
import { Card, CardContent, Typography, Grid, Button } from '@mui/material';
import { Warning, CheckCircle, Person } from '@mui/icons-material';
import io from 'socket.io-client';

export default function Dashboard() {
  const router = useRouter();
  const [stats, setStats] = useState({
    totalStudents: 120,
    alertsToday: 5,
    activeCameras: 4
  });
  
  const [recentAlerts, setRecentAlerts] = useState<any[]>([]);

  useEffect(() => {
    // Socket connection
    const socket = io('http://localhost:8000', { path: '/ws/alerts' });
    
    socket.on('connect', () => {
      console.log('Connected to WebSocket');
    });

    socket.on('ALERT_NEW', (message: any) => {
      // Handle new alert
      const data = JSON.parse(message).data;
      setRecentAlerts(prev => [data, ...prev].slice(0, 5));
      setStats(prev => ({ ...prev, alertsToday: prev.alertsToday + 1 }));
    });

    return () => {
      socket.disconnect();
    };
  }, []);

  return (
    <div className="p-8 bg-slate-50 min-h-screen">
      <header className="flex justify-between items-center mb-8">
        <h1 className="text-3xl font-bold text-slate-800">School Security Dashboard</h1>
        <Button variant="contained" color="primary" onClick={() => router.push('/live')}>
          View Live Feed
        </Button>
      </header>

      <Grid container spacing={3} className="mb-8">
        <Grid item xs={12} md={4}>
          <Card className="bg-white shadow-md">
            <CardContent className="flex items-center gap-4">
              <Person fontSize="large" className="text-blue-500" />
              <div>
                <Typography color="textSecondary">Total Students Detected</Typography>
                <Typography variant="h4">{stats.totalStudents}</Typography>
              </div>
            </CardContent>
          </Card>
        </Grid>
        <Grid item xs={12} md={4}>
          <Card className="bg-white shadow-md">
            <CardContent className="flex items-center gap-4">
              <Warning fontSize="large" className="text-red-500" />
              <div>
                <Typography color="textSecondary">Alerts Today</Typography>
                <Typography variant="h4">{stats.alertsToday}</Typography>
              </div>
            </CardContent>
          </Card>
        </Grid>
        <Grid item xs={12} md={4}>
          <Card className="bg-white shadow-md">
            <CardContent className="flex items-center gap-4">
              <CheckCircle fontSize="large" className="text-green-500" />
              <div>
                <Typography color="textSecondary">System Status</Typography>
                <Typography variant="h4" className="text-green-600">Active</Typography>
              </div>
            </CardContent>
          </Card>
        </Grid>
      </Grid>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
        <section>
          <h2 className="text-xl font-semibold mb-4 text-slate-700">Recent Alerts</h2>
          <div className="space-y-4">
            {recentAlerts.map((alert, idx) => (
              <div key={idx} className="bg-white p-4 rounded shadow border-l-4 border-red-500 flex gap-4">
                <div className="w-16 h-16 bg-gray-200 rounded overflow-hidden">
                    {/* eslint-disable-next-line @next/next/no-img-element */}
                    <img src={`http://localhost:8000/${alert.snapshot}`} alt="Alert" className="object-cover w-full h-full" />
                </div>
                <div>
                  <h3 className="font-bold text-red-600">{alert.type.replace('_', ' ')}</h3>
                  <p className="text-sm text-gray-500">{alert.location} - {new Date(alert.timestamp).toLocaleTimeString()}</p>
                </div>
              </div>
            ))}
            {recentAlerts.length === 0 && <p className="text-gray-400">No recent alerts.</p>}
          </div>
        </section>

        <section>
          <h2 className="text-xl font-semibold mb-4 text-slate-700">Quick Actions</h2>
          <div className="grid grid-cols-2 gap-4">
            <Button variant="outlined" className="h-24">Manage Faces</Button>
            <Button variant="outlined" className="h-24">Camera Settings</Button>
            <Button variant="outlined" className="h-24">View Logs</Button>
            <Button variant="outlined" className="h-24 text-red-500 border-red-200 hover:bg-red-50">Emergency Mode</Button>
          </div>
        </section>
      </div>
    </div>
  );
}
