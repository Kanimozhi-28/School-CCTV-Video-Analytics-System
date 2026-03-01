'use client';
import { useState } from 'react';
import { Card, CardContent, TextField, Button, Grid, MenuItem, Typography, Alert } from '@mui/material';
import axios from 'axios';

export default function FaceManagement() {
    const [tab, setTab] = useState('student');
    const [formData, setFormData] = useState({
        name: '',
        grade: '',
        relationship: 'Father',
        phone_number: '',
        student_id: '',
    });
    const [file, setFile] = useState<File | null>(null);
    const [message, setMessage] = useState<{ type: 'success' | 'error', text: string } | null>(null);

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        if (!file) return setMessage({ type: 'error', text: 'Please select an image' });

        const data = new FormData();
        data.append('file', file);
        data.append('name', formData.name);

        let url = 'http://localhost:8000/api/faces/register/student';
        if (tab === 'student') {
            data.append('grade', formData.grade);
        } else {
            url = 'http://localhost:8000/api/faces/register/parent';
            data.append('relationship', formData.relationship);
            data.append('phone_number', formData.phone_number);
            data.append('student_id', formData.student_id);
        }

        try {
            const res = await axios.post(url, data, {
                headers: { 'Content-Type': 'multipart/form-data' }
            });
            setMessage({ type: 'success', text: `Successfully registered ${res.data.name}` });
            // reset form
        } catch (err: any) {
            console.error(err);
            setMessage({ type: 'error', text: err.response?.data?.detail || 'Registration failed' });
        }
    };

    return (
        <div className="p-8 max-w-4xl mx-auto">
            <h1 className="text-3xl font-bold mb-8 text-slate-800">Face Database Management</h1>

            <div className="flex gap-4 mb-6">
                <Button
                    variant={tab === 'student' ? 'contained' : 'outlined'}
                    onClick={() => setTab('student')}
                >
                    Add Student
                </Button>
                <Button
                    variant={tab === 'parent' ? 'contained' : 'outlined'}
                    onClick={() => setTab('parent')}
                >
                    Add Parent/Guardian
                </Button>
            </div>

            <Card>
                <CardContent className="space-y-6">
                    <Typography variant="h6" className="mb-4">
                        {tab === 'student' ? 'New Student Registration' : 'New Guardian Registration'}
                    </Typography>

                    {message && <Alert severity={message.type}>{message.text}</Alert>}

                    <form onSubmit={handleSubmit} className="space-y-4">
                        <Grid container spacing={3}>
                            <Grid item xs={12} md={6}>
                                <TextField
                                    label="Full Name"
                                    fullWidth
                                    required
                                    value={formData.name}
                                    onChange={(e) => setFormData({ ...formData, name: e.target.value })}
                                />
                            </Grid>

                            {tab === 'student' && (
                                <Grid item xs={12} md={6}>
                                    <TextField
                                        label="Grade / Class"
                                        fullWidth
                                        required
                                        value={formData.grade}
                                        onChange={(e) => setFormData({ ...formData, grade: e.target.value })}
                                    />
                                </Grid>
                            )}

                            {tab === 'parent' && (
                                <>
                                    <Grid item xs={12} md={6}>
                                        <TextField
                                            select
                                            label="Relationship"
                                            fullWidth
                                            value={formData.relationship}
                                            onChange={(e) => setFormData({ ...formData, relationship: e.target.value })}
                                        >
                                            <MenuItem value="Father">Father</MenuItem>
                                            <MenuItem value="Mother">Mother</MenuItem>
                                            <MenuItem value="Guardian">Guardian</MenuItem>
                                        </TextField>
                                    </Grid>
                                    <Grid item xs={12} md={6}>
                                        <TextField
                                            label="Phone Number"
                                            fullWidth
                                            required
                                            value={formData.phone_number}
                                            onChange={(e) => setFormData({ ...formData, phone_number: e.target.value })}
                                        />
                                    </Grid>
                                    <Grid item xs={12} md={6}>
                                        <TextField
                                            label="Linked Student ID"
                                            fullWidth
                                            required
                                            type="number"
                                            value={formData.student_id}
                                            onChange={(e) => setFormData({ ...formData, student_id: e.target.value })}
                                        />
                                    </Grid>
                                </>
                            )}

                            <Grid item xs={12}>
                                <label className="block mb-2 text-sm font-medium text-gray-900">Upload Face Photo</label>
                                <input
                                    type="file"
                                    accept="image/*"
                                    required
                                    onChange={(e) => setFile(e.target.files?.[0] || null)}
                                    className="block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 focus:outline-none"
                                />
                                <p className="mt-1 text-sm text-gray-500">Ensure face is clearly visible and well-lit.</p>
                            </Grid>

                            <Grid item xs={12}>
                                <Button type="submit" variant="contained" color="secondary" size="large" fullWidth>
                                    Register Profile
                                </Button>
                            </Grid>
                        </Grid>
                    </form>
                </CardContent>
            </Card>
        </div>
    );
}
