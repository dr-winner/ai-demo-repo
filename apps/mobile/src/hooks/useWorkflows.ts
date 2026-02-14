import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { WorkflowService } from '../services/workflow.service';
import type { CreateRunPayload } from '@life-os/shared-types';

export const WORKFLOW_KEYS = {
  all: ['workflows'] as const,
  runs: () => [...WORKFLOW_KEYS.all, 'runs'] as const,
  run: (id: string) => [...WORKFLOW_KEYS.runs(), id] as const,
  steps: (runId: string) => [...WORKFLOW_KEYS.run(runId), 'steps'] as const,
};

export const useWorkflowRuns = (skip = 0, limit = 10) => {
  return useQuery({
    queryKey: [...WORKFLOW_KEYS.runs(), { skip, limit }],
    queryFn: () => WorkflowService.listRuns(skip, limit),
  });
};

export const useWorkflowRun = (runId: string | null) => {
  return useQuery({
    queryKey: WORKFLOW_KEYS.run(runId!),
    queryFn: () => WorkflowService.getRun(runId!),
    enabled: !!runId,
  });
};

export const useWorkflowSteps = (runId: string | null) => {
  return useQuery({
    queryKey: WORKFLOW_KEYS.steps(runId!),
    queryFn: () => WorkflowService.listSteps(runId!),
    enabled: !!runId,
  });
};

export const useCreateWorkflowRun = () => {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: (payload: CreateRunPayload) => WorkflowService.createRun(payload),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: WORKFLOW_KEYS.runs() });
    },
  });
};
