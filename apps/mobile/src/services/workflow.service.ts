import { apiClient } from '../lib/api/client';
import type {
  WorkflowRun,
  WorkflowStep,
  CreateRunPayload,
  PaginatedResponse,
} from '@life-os/shared-types'; // Importing from shared package

export const WorkflowService = {
  // ── Workflow Runs ────────────────────────────────

  listRuns: async (skip: number = 0, limit: number = 10): Promise<PaginatedResponse<WorkflowRun> | WorkflowRun[]> => {
    // The previous implementation returned PaginatedResponse, but let's be robust
    return apiClient.get('/api/v1/runs', {
      params: { skip, limit },
    });
  },

  getRun: async (runId: string): Promise<WorkflowRun> => {
    return apiClient.get(`/api/v1/runs/${runId}`);
  },

  createRun: async (payload: CreateRunPayload): Promise<WorkflowRun> => {
    return apiClient.post('/api/v1/runs', payload);
  },

  // ── Workflow Steps ───────────────────────────────

  listSteps: async (runId: string): Promise<WorkflowStep[]> => {
    return apiClient.get('/api/v1/steps', {
      params: { run_id: runId },
    });
  },

  getStep: async (stepId: string): Promise<WorkflowStep> => {
    return apiClient.get(`/api/v1/steps/${stepId}`);
  },
};
